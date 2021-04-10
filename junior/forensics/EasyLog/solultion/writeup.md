# EasyLog writeup
At the first glance, we can understand that this is a Flask access log. It shows user's actions on your website. 
The second thing we have to do is to try to find pages like 'flag', 'admin', 'passwords', etc. In this particular task, we have two interesting requests: 'flag' and 'admin'. So now, all that remains to be done is to connect to the following links: http://77.223.96.24:21006/flag and http://77.223.96.24:21006/admin. The real flag is located in the second one.

Flag: **flag{d1d_y0u_3nj0y_0ur_l0g5?_1_h0p3_y0u_d1d}**
