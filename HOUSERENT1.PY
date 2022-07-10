option={1:"Owner", 2: "Tenant", 3:"Approver"}
mylist_home=[]
add_home=[]
class main_class:

    print("WELCOME to our page!!!\n")

    def available_home(self):
        print()
        if len(mylist_home)==0:
            print("Not available!")
            return False
        for index,keyval in enumerate(mylist_home):
            print("Home No:{0} Details:{1}".format(index,keyval))
        return True


class Owner:

    def home_details(self):
        home={}
        home["City"]=input("Enter City:")
        home["type_home"]=input("\nEnter house type:")
        home["Sqft"]=input("Enter Square Feet:")
        home["Rent"]=input("Enter Rent:")
        mylist_home.append(home)
        print("\nHome detail added Successfully!!")
        self.user_options(1)

    def remove_home(self):
        print("\nEnter Home details:")
        if self.available_home():
            home_no=int(input("Enter home number to remove: "))
            mylist_home.pop(home_no)
            print("\nHome detail Removed Successfully!!")
        self.user_options(1)

    def view_HomeDetails(self):
        print("\nRental Requests:")
        if len(add_home)==0:
            print("Not available")
        else:
            for index,key in enumerate(add_home):
                print("Request No: {0} Request: {1}".format(index,key))
        self.user_options(1)



class Tenant:

    def rent_request(self):
        self.available_home()
        request={}
        request["Name"]=input("\nEnter Name: ")
        request["Home No"]=input("Enter Home No: ")
        request["Home location"]=input("Enter home location: ")

        add_home.append(request)
        print("\nRequest Submitted Successfully!!")


class choice(main_class,Owner,Tenant):
    home=[]
    def options(self):
        for key,val in option.items():
            print("{0}. {1}".format(key,val))
        choice_user=int(input("Enter option:"))
        print("\nWelcome {0}".format(option[choice_user]))
        self.user_options(choice_user)



    def user_options(self,user_type):
        if user_type==1:
            print("\nowner Options:")
            print("1. Home details")
            print("2. Remove")
            print("3. View details")
            option=int(input("\nEnter option number:"))
            if option==1:
                self.home_details()
            elif option==2:
                self.remove_home()
            elif option==3:
                self.view_HomeDetails()



        elif user_type==2:
            print("\nOptions:")
            print("1. Request for house")
            print("2. Quit")
            option=int(input("Enter option number: "))
            self.rent_request() if option==1 else self.options()

if __name__=="__main__":
    x=choice()
    x.options()
