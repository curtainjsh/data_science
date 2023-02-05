def solution(S) :
    # Declare parallel list to store total seconds and phone numbers
    call_durations =  []
    phone_numbers =  []
    formatted_phone_numbers =  []
    formatted_call_durations =  []
    # creating a HashTable Dictionary to calculate total seconds for each phone number
    total_durations =  dict()
    # use scanner to split using line separator
    scanner =  "Python-inputs".useDelimiter(System.lineSeparator())
    lines = S.split('\n')

    # Loop until it has line
    while (scanner.hasNextLine()) :
        line = input()
        lineTokens = line.split("[,]",0)
        # tokens[0] - will be in format hh:mm:ss
        formatted_call_durations.append(lineTokens[0])
        durationTokens = lineTokens[0].split(":")
        # convert into int values
        hours = int(durationTokens[0])
        minutes = int(durationTokens[1])
        seconds = int(durationTokens[2])
        totalDuration = (hours * 60 * 60) + (minutes * 60) + seconds
        # Add the values to arraylist
        call_durations.append(totalDuration)
        # tokens[0] - will be in format nnn-nnn-nnn
        formatted_phone_numbers.append(lineTokens[1])
        phoneNumber = int(lineTokens[1].replace("-",""))
        phone_numbers.append(phoneNumber)
        # get all the previous total durations for this number
        previousTotal = total_durations.get(phoneNumber)
        # if the map contains no mapping for the key, add the key and value
        if (previousTotal == None) :
            total_durations.put(phoneNumber,totalDuration)
        else :
            total_durations.put(phoneNumber,previousTotal + totalDuration)
    # Close the scanner
    scanner.close()
    # find which phone number has longest duration
    promo_phone = 0
    longduration = 0
    print(String.format("%-15s  %15s","Phone Number","Total Call Duration(Seconds)"))
    for phone in total_durations.keySet() :
        # Assume first phone is promo
        # or current phone has longest duration
        # or (duration is equal and smallest phone)
        if (promo_phone == 0 or total_durations.get(phone) > longduration or (total_durations.get(phone) == longduration and phone < promo_phone)) :
            promo_phone = phone
            longduration = total_durations.get(phone)
        print(String.format("%-15d  %15d",phone,total_durations.get(phone)))
    print()
    print("Promo applied phone number: " + str(promo_phone))
    # Calculate amount excluding promo applied to the longest duration phone number
    totalCharge = 0
    print()
    print(String.format("%-15s  %15s %20s","Phone Number","Call Duration","Charge (In Cents) "))
    index = 0
    while (index < len(call_durations)) :
        # Calculate based duration
        call_charge = 0
        # if the corresponding is promo applied, do not calculate
        if (promo_phone != phone_numbers[index]) :
            # if less than 5 minutes (300 seconds), pay 3 cents for every seconds
            if (call_durations[index] < 300) :
                call_charge = call_durations[index] * 3
            else :
                # Convert the secomds to minutes
                toalMinutes = int(call_durations[index] / 60)
                # have to pay, even if minute is started
                if (call_durations[index] % 60 > 0) :
                    toalMinutes += 1
                # Pay 150 cents for every started call
                call_charge = toalMinutes * 150
            # add to total charge
            totalCharge += call_charge
        # print the values on console
        print(String.format("%-15s  %15s %10d",formatted_phone_numbers[index],formatted_call_durations[index],call_charge))
        index += 1
    # return the total charge
    return totalCharge
S = '00:01:07,400-234-290'
solution(S)
