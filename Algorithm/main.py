data = """
#1.1 Securing the Keys (05:07)

#1.2 Router Setup (09:59)
#2 AUTHENTICATION

#2.0 Using Firebase Auth (08:36)

#2.1 Login Form part One (07:57)

h + ':' + m + ':' + scap (04:04)

#2.3 Creating Account (09:41)

#2.4 Log In (10:36)

#2.5 Social Login (07:09)

#2.6 Log Out (06:37)
#3 NWEETING

#3.0 Form and Database Setup (04:34)

#3.1 Nweeting! (06:37)

#3.2 Getting the Nweets (08:32)

#3.3 Realtime Nweets (11:52)

#3.4 Delete and Update part One (05:44)

#3.5 Delete and Update part Two (11:12)

#3.6 Recap (07:58)
#4 FILE UPLOAD

#4.0 Preview Images part One (07:49)

#4.1 Preview Images part Two (05:51)

#4.2 Uploading (09:04)

#4.3 File URL and Nweet (08:37)

#4.4 Deleting Files (05:47)
#5 EDIT PROFILE

#5.0 Get My Own Nweets (10:33)

#5.1 Update Profile (08:52)

#5.2 Update Profile Bugfix (11:23)
#6 FINISHING UP

#6.0 Cleaning JS (08:54)

#6.1 Styles (05:12)

#6.2 Deploying (05:43)

#6.3 Security on Firebase (08:24)

#6.4 API Key Security (03:23)

#6.5 Conclusions (05:42)
"""

m, s = 0, 0
for t in data.splitlines():
    if not t:
        continue
    if t[-1] == ")":
        m += int(t[-6:-4])
        s += int(t[-3:-1])

m += s // 60
s = s % 60
h = m // 60
m = m % 60
print(str(h) + ":" + str(m) + ":" + str(s))
