-- Create the database hbtn_0d_2 and user user_0d_2
-- user_0d_2 should have password user_od_2_pwd
-- if either data exists not to fail
CREATE  DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
