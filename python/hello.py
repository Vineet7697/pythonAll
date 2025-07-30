website = input("Enter website name: ").lower()

if website=="amazon":
    website = input("Enter product or service: ").lower()
    
    if website=="product":
        website = input("Enter clothes or shoes: ").lower()
        
        if website=="clothes":
            print("2000")
        elif website=="shoes":
            print("1000")
        else:
            print("Invavlid")
    
    elif website=="service":
        print("Not available")
    
    else:
        print("Invalid")
    
else:
    print("Invalid")