# Assignment 3

### GET responses

http://192.168.99.100:5002/v1/expenses/1 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo1@bar.com", 
  "estimated_costs": "800", 
  "id": 1, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 1", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}

http://192.168.99.100:5002/v1/expenses/2 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo2@bar.com", 
  "estimated_costs": "800", 
  "id": 2, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 2", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}

http://192.168.99.100:5002/v1/expenses/3 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo3@bar.com", 
  "estimated_costs": "800", 
  "id": 3, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 3", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}

http://192.168.99.100:5003/v1/expenses/4 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo4@bar.com", 
  "estimated_costs": "800", 
  "id": 4, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 4", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}

http://192.168.99.100:5002/v1/expenses/5 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo5@bar.com", 
  "estimated_costs": "800", 
  "id": 5, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 5", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}

http://192.168.99.100:5001/v1/expenses/6 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo6@bar.com", 
  "estimated_costs": "800", 
  "id": 6, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 6", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}

http://192.168.99.100:5003/v1/expenses/7 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo7@bar.com", 
  "estimated_costs": "800", 
  "id": 7, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 7", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}

http://192.168.99.100:5002/v1/expenses/8 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo8@bar.com", 
  "estimated_costs": "800", 
  "id": 8, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 8", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}

http://192.168.99.100:5003/v1/expenses/9 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo9@bar.com", 
  "estimated_costs": "800", 
  "id": 9, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 9", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}

http://192.168.99.100:5002/v1/expenses/10 200
{
  "category": "office supplies", 
  "decision_date": "2016-12-17", 
  "description": "iPad for office use", 
  "email": "foo10@bar.com", 
  "estimated_costs": "800", 
  "id": 10, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo 10", 
  "status": "pending|approved|rejected|overbudget", 
  "submit_date": "12-10-2016"
}


Process finished with exit code 0

------------------------------------------------------------------------------------------
Steps to run the code :

--- mkdir 3 directories at below paths for 3 instances of mysql ---

/mnt/sda1/var/mysql_data1

/mnt/sda1/var/mysql_data2

/mnt/sda1/var/mysql_data3


--- starting 3 mysql instances ---

docker run --name db1 -v /mnt/sda1/var/mysql_data1:/var/lib/mysql -e MYSQL_USER=root -e MYSQL_ROOT_PASSWORD=pass1234 -e MYSQL_ROOT_HOST=% -it -p 3306:3306 -d mysql

docker run --name db2 -v /mnt/sda1/var/mysql_data2:/var/lib/mysql -e MYSQL_USER=root -e MYSQL_ROOT_PASSWORD=pass1234 -e MYSQL_ROOT_HOST=% -it -p 3307:3306 -d mysql

docker run --name db3 -v /mnt/sda1/var/mysql_data3:/var/lib/mysql -e MYSQL_USER=root -e MYSQL_ROOT_PASSWORD=pass1234 -e MYSQL_ROOT_HOST=% -it -p 3308:3306 -d mysql

--- 3 instances of assignment1 ---

cd assignment1App1ForAssign3

docker build -t app1 .

docker run -d -p 5001:5001 --name app1 -e PYTHONUNBUFFERED=0 --link db1:mysql -d app1

cd ..


cd assignment1App2ForAssign3

docker build -t app2 .

docker run -d -p 5002:5002 --name app2 -e PYTHONUNBUFFERED=0 --link db2:mysql -d app2

cd ..


cd assignment1App3ForAssign3

docker build -t app3 .

docker run -d -p 5003:5003 --name app3 -e PYTHONUNBUFFERED=0 --link db3:mysql -d app3

cd ..


--- main program ---

cd assignment3

python ch_client.py
---------------------------------------------------------------------------------------------------------------------

3 instances run at below mentioned ports:

instance 1 of assignment 1 : 192.168.99.100:5001

instance 2 of assignment 1 : 192.168.99.100:5002

instance 3 of assignment 1 : 192.168.99.100:5003

---------------------------------------------------------------------------------------------------------------------