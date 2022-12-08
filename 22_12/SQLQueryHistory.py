SELECT * FROM blog_signup WHERE BtcValue IS NULL


SELECT COUNT(*) FROM blog_signup WHERE username LIKE 'G-%'

SELECT username FROM blog_signup WHERE username ="G-chlrjs23@gmail.com"

UPDATE blog_signup SET username = REPLACE(username, 'G-', "")

UPDATE blog_signup SET BtcValue = "0" WHERE BtcValue IS NULL;

# mongoDB
mongorestore -d name bson경로


