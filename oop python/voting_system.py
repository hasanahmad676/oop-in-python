# create voting system

nominee_1 = input("Enter the first nominee: ")
nominee_2 = input("Enter the second nominee: ")
nominee_1_votes = 0
nominee_2_votes = 0
voter_id = [1,2,3,4,5,6,7,8,9]
no_of_voters = len(voter_id)

while True:
    if voter_id == []:
        print("Voting is over")
        if nominee_1_votes > nominee_2_votes:
            percentage = nominee_1_votes / no_of_voters * 100
            print("The winner is: ", nominee_1,"with", percentage, "% of votes")
            break
        elif nominee_1_votes < nominee_2_votes:
            percentage = nominee_2_votes / no_of_voters * 100
            print("The winner is: ", nominee_2,"with", percentage, "% of votes")
            break
        else:
            print("The votes are tied")
            break
             
    voter=int(input("Enter voter id: "))
    if voter in voter_id:
        print("you're already voter")
        voter_id.remove(voter)
        print("----------------------------------------")
        print("For giving vote to", nominee_1,"Press 1")
        print("For giving vote to", nominee_2,"Press 2")
        print("----------------------------------------")
        vote=int(input("Enter your vote: "))
        if vote == 1:
            nominee_1_votes += 1
            print(nominee_1,"got",nominee_1_votes,"votes")
            print(nominee_1,"Thank you to give your precious vote to him")
        elif vote == 2:
            nominee_2_votes += 1
            print(nominee_2,"got",nominee_2_votes,"votes")
            print(nominee_2,"Thank you to give your precious vote to him")
        elif vote > 2:
            print("check your pressed key or invalid key ")
        else:
            print("you are already give your vote")
 
    

         
