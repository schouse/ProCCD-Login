import sys, traceback
from PySide2.QtCore import *
from GUI_Main import *

class ThreadFunctions():

    overlayReady = 0 # Whether a particular processing result can be overlaid (f.e., thresholding, but not blurring)
    temporaryImg = 0

    def histogram_wrapper(self):
        self.overlayReady = 1 # Can be overlaid
        worker = Worker(self.updateHistogram)  # Any other args, kwargs are passed to the run function
        worker.signals.resultThread.connect(self.print_output)
        worker.signals.finishedThread.connect(self.thread_complete) # Merely shows thread is done
        worker.signals.progressThread.connect(self.progress_fn) # Doesn't do anything yet. Used for Progress Bars
        # Execute
        self.threadpool.start(worker)


    # def distanceTrans_wrapper(self):
    #     # Pass the function to execute
    #     self.overlayReady = 0 # Should not be overlaid
    #     worker = Worker(self.distanceT, self.latestProcImg)  # Any other args, kwargs are passed to the run function
    #     worker.signals.resultThread.connect(lambda result: self.print_output(result))
    #     worker.signals.finishedThread.connect(self.thread_complete) # Merely shows thread is done
    #     worker.signals.progressThread.connect(self.progress_fn) # Doesn't do anything yet. Used for Progress Bars
    #     # Execute
    #     self.threadpool.start(worker)


    def thread_complete(self):
        # self.ui.dockFeatureDisplay.setEnabled(True)
        # self.ui.statusBar.showMessage("Histogram Updated")
        # print("Histogram Updated")
        pass

    def print_output(self):
        # print("Ready to show image")
        # self.showLatestProcessedImage(img)
        # print("Histogram done")
        pass

    def progress_fn(self):
        # self.ui.dockFeatureDisplay.setEnabled(False)
        # self.ui.statusBar.showMessage("Updating Histogram")
        # print("Histogram being updated")
        pass

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
        Supported signals are:
            finished
                No data
            error
                `tuple` (exctype, value, traceback.format_exc() )
            result
                `object` data returned from processing, anything
            progress
                `int` indicating % progress
    '''
    finishedThread = Signal()
    errorThread = Signal(tuple)
    # resultThread = Signal(object) # resultThread will be an object if after processing some result is there like processed image
    resultThread = Signal() # otherwise resultThread is without any object
    progressThread = Signal()

class Worker(QRunnable):
    '''
    Worker thread
    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
        :param callback: The function callback to run on this worker thread. Supplied args and
                         kwargs will be passed through to the runner.
        :type callback: function
        :param args: Arguments to pass to the callback function
        :param kwargs: Keywords to pass to the callback function
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        # Add the callback to our kwargs
        # self.kwargs['progress_callback'] = self.signals.progressThread

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        # result = self.fn(*self.args, **self.kwargs)

        # Retrieve args/kwargs here; and fire processing using them
        self.signals.progressThread.emit()
        try:
            # processed_image = self.fn(*self.args, **self.kwargs) # Some problem
            self.fn()
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.errorThread.emit((exctype, value, traceback.format_exc()))
        else:
            # self.signals.resultThread.emit(processed_image)  # Return the result of the processing
            self.signals.resultThread.emit()  # Return the result of the processing
        finally:
            self.signals.finishedThread.emit()  # Done

