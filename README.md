# chatbot-with-microservices
 A dentist reservation chatbot combined with two techniques( flow based and machine learning based ) 

## Deployment

1. Directory  
-- chatBotApi  
-- frontend  
-- service1  
-- service2  
3. For Service1(dentists resource):
```
cd service1
docker build -t service1 . 
docker run -p 5001:5000 -t service1
```
3. For service2(timeslots resource):
```
cd ..
cd service2
docker build -t service2 . 
docker run -p 5002:5000 -t service2
```
4. For chatbot Api
```
cd ..
cd chatBotApi
cd chatbotApi
pip install -r requirements.txt
cd chatbotApi
python3 __init__.py
```
5. For frontend
```
cd ../../../frontend
open index.html in browser
(CROS has been fixed in backend part)
```  

## Features
Note: the button in frontend page only works once, please copy text in button and paste
it in input field, then click icon or press Enter to send message.

1. Greeting:
Input Hello or similar word(based on Wit.ai)  

2. List all the available doctors:  
Input Dentists Information

3. Retrive information about one doctor:  
Input Dr. Alex

4. Already reserved（chatbot reply all available time except reserved time)   
5. Available timeslots  
Like previous one

6. Summarize booking Information  
When input 12:00 pm. Chatbot will reply summarized infomation  

7. Cancel the booking  

8. Swagger API document  

![feature 1!](https://raw.githubusercontent.com/u17zl/chatbot-with-microservices/master/images/img_1.png "Feature 1")
![feature 2!](https://raw.githubusercontent.com/u17zl/chatbot-with-microservices/master/images/img_2.png "Feature 2")  
![feature 3!](https://raw.githubusercontent.com/u17zl/chatbot-with-microservices/master/images/img_3.png "Feature 3")
![feature 4!](https://raw.githubusercontent.com/u17zl/chatbot-with-microservices/master/images/img_4.png "Feature 4")  
![feature 5!](https://raw.githubusercontent.com/u17zl/chatbot-with-microservices/master/images/img_5.png "Feature 5")  
![feature 6!](https://raw.githubusercontent.com/u17zl/chatbot-with-microservices/master/images/img_6.png "Feature 6")  
![feature 7!](https://raw.githubusercontent.com/u17zl/chatbot-with-microservices/master/images/img_7.png "Feature 7")  
![feature 8!](https://raw.githubusercontent.com/u17zl/chatbot-with-microservices/master/images/img_8.png "Feature 8")  
![feature 9!](https://raw.githubusercontent.com/u17zl/chatbot-with-microservices/master/images/img_9.png "Feature 9")
