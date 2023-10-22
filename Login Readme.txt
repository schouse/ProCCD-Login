=========== Documentation for login authentication system ===========

1. At the top the database and tables are being created with functionality if Doesn't exist.
	The tables which are created and being used :
		1. auth_user ( Basically user table with id, password, user_group, created time stamp etc.)
		2. requests ( A table with requests from users to admin, such as pw reset, login count reset, etc.)
		3. login_count ( A table that records the login attempts )
		4. action_record (A table that records all the actions done by the user in the main app)
		5. login_record (A table which records all the login attempts, login failed, password changing by user)

2. The class "AdminPanel" is defined with methods that are being used to execute operations that an admin can do like export records, add a new user, show login records, show user list, change or reset password of a particular user, delete a user etc.

3. Then a class "ForgetPassword" is created with some methods to show the forget password window and do operations like change password, ask admin to reset password etc also handles some complications like if the input is empty or not, new password matches the criteria or not etc and throw messages to the user.

4. "Login" class is created which opens the first window at the start where the user can log in, it has a method "login" which handles all the logins. It handles the attempts of logins done by a user from a host, records the count of login attempts and if attempts are more than 5 times with wrong credentials it blocks that particular host to login in further. Also on successful login, it redirects to the admin panel if the logged user is an admin, or it redirects to the main app if the logged user is not admin. It also stores the login records.

5. There are also some methods which are called on demand to open or close windows as per needed.


Credentials (Admin) admin/12345678
Credentials (User)  user/12345678
