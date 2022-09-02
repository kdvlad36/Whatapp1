from email import message
import pywhatkit
global recipient_list

recipient_list = []
with open('recipient_list.txt', 'r', encoding='utf8') as f:
	for number in f:
		number = number.replace('[', '').replace('\'', '').replace(']', '').replace('\n', '')

		recipient_list.append(number)
        
def send_message_inst():
    mobile = number
    message = 'Привет '
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)
    
def main():
    send_message_inst()
    # send_message()

    # pywhatkit.image_to_ascii_art(img_path='hack_achiv.png')
    
    
if __name__ == '__main__':
    main()
import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))