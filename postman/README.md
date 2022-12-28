# Cases generation(data preprocessing for the Postman)
## Basic Information：
### Original Payload
* application
* credit(include different stages, depends on specific condition)

### Environment 
* the environment variables exported from postman

### Ckpt
* store all the output request bodies

### Case db(from SQL Server)
* input : original cases information 
* output : filtered cases information

## Usage：
### *main.py*
First of all, you are supposed to have a piece of environment variables and a specific stage of original payload(i.e. the stage you want to put your request body in), and you would mainly use *main.py* to start your works. Before running the *main.py*, make sure you check all the file paths.

### *case_info.py* 
After using "postman" to apply cases, you should fetch the cases information from SQL Server(i.e. export csv files to the *case_db/input*).Now, just run *case_info.py* to get a filtered data and import it to the postman, then make postman do the credit reviews.

Have fun!

