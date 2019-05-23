#"Cycle" by BitWorks Game Studios
from gamelib import*    
game=Game(1280,720,"BitWorks' Cycle")
#Images
bk2=Image("bk2.png",game)
bwgs=Image("BitWorks.png",game)
logo=Image("Violet.png",game)
begin=Image("press_space.png",game)
door_r=Image("Door1.png",game)
door_l=Image("Door2.png",game)
black=Image("black.jpg",game)
#Resize
bwgs.resizeBy(-10)
logo.resizeBy(-30)
begin.resizeBy(-60)
door_r.resizeBy(1000)
door_l.resizeBy(1000)
bk2.resizeTo(game.width,game.height)
black.resizeTo(game.width,game.height)
#Character Variables
Age=10
Health=("Stable")
Quality=("Good")
Financial=("Good")
Education=("None")
Job=("None")
health=50
quality=50
financial=50
job=0
#Stats
class stats(object):
    def start():
        #Health
        if health<30:
            Health=("Very Damaging")
        if health<40 and health>30:
            Health=("Damaging")
        if health<70 and health>40:
            Health=("Stable")
        if health<100 and health>70:
            Health=("Very Stable")
        #Quality of Life
        if quality<30:
            Quality=("Very Unpleasing")
        if quality<40 and quality>30:
            Quality=("Bad")
        if quality<70 and quality>40:
            Quality=("Good")
        if quality<100 and quality>70:
            Quality=("Pleasing")
        #Finantial Status
        if financial<30:
            Financial=("Bad")
        if financial<40 and financial>30:
            Financial=("OK")
        if financial<70 and financial>40:
            Financial=("Good")
        if financial<100 and financial>70:
            Financial=("Pleasing")
        #Job
        if job<1:
            Job=("None")
        if job<30 and job>1:
            Job=("Terrible")
        if job>30 and job<40:
            Job=("OK")
        if job<70 and job>40:
            Job=("Good")
        if job<100 and job>70:
            Job=("Pleasing and Stable")
#Fonts
Font1=Font(white,30,black,"Courier New")
Font2=Font(white,50,black,"Courier New")
Font3=Font(white,25,black,"Courier New")
#Doors
doors_r=[]
for index in range(100):
    doors_r.append(Image("Door1.png",game))
    doors_r[index].resizeBy(1500)
    doors_r[index].moveTo(200,400)
doors_l=[]
for index in range(100):
    doors_l.append(Image("Door2.png",game))
    doors_l[index].resizeBy(1500)
    doors_l[index].moveTo(1080,400)
#Main Menu
while not game.over:
    game.processInput()
    bk2.draw()
    for index in range(1):
        door_r.moveTo(game.width/2,300)
        door_r.draw()
    game.drawText("Cycle",560,door_r.y,Font2)
    game.drawText("PRESS [SPACE] TO BEGIN YOUR STORY",170,550,Font2)
    game.drawText("2019 BitWorks",450,650,Font2)
    if keys.Pressed[K_SPACE]:
        game.over=True
    game.update(30)
game.over=False
#Tutorial1
while not game.over:
    game.processInput()
    dr=True
    bk2.draw()
    game.drawText("Use The Left Mouse Button to Click One of the Doors and Make a Decision",100,10,Font3)
    for index in range(1):
        doors_r[index].draw()
    for index in range(1):
        doors_l[index].draw()
    game.drawText("PRESS [2] TO CONTINUE",300,600,Font2)
    if keys.Pressed[K_2]:
        game.over=True
    game.update(30)
game.over=False
#Tutorial2
while not game.over:
    game.processInput()
    dr=True
    bk2.draw()
    game.drawText("Your Actions Affect Your Stats, Be Careful",150,10,Font1)
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    for index in range(1):
        doors_r[index].draw()
    for index in range(1):
        doors_l[index].draw()
    game.drawText("PRESS [3] TO PLAY",350,650,Font2)
    if keys.Pressed[K_3]:
        #WATCH OUT WATCH OUT WATCH OUT
        dead1=True
        game.over=True
    game.update(30)
game.over=False
#Game Start
#>Age:10
#BREAKFAST TIME
while not game.over:
    game.processInput()
    bk2.draw()
    Education=("5th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            health-=1
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice 2
            Age+1
            health+=1
            game.over=True
    #Decision
    game.drawText("Breakfast Time",400,30,Font2)
    #Choices
    #Left Choice
    game.drawText("Pancakes and Bacon",50,80,Font3)
    #Right Choice
    game.drawText("Bowl of Fruit",930,80,Font3)
    game.update(30)
game.over=False
#>Age:11
#YOU FORGOT YOUR HW
while not game.over:
    game.processInput()
    bk2.draw()
    Education=("6th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            hw=False
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice 2
            Age+=1
            hw=True
            game.over=True
    #Decision
    game.drawText("You Forgot To Do Your HW",300,30,Font2)
    #Choices
    #Left Choice
    game.drawText("One Day Won't Hurt",50,80,Font3)
    #Right Choice
    game.drawText("Hurry Up And Do It",930,80,Font3)
    game.update(30)
game.over=False
#>Age:12
#THE TEACHER COLLECTS HW
while not game.over and not hw:
    game.processInput()
    bk2.draw()
    Education=("7th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age=+1
            w=True
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice 2
            Age+=1
            w=True
            game.over=True
    #Decision
    game.drawText("The Teacher Collects HW",350,30,Font2)
    #Choices
    #Left Choice
    game.drawText("Give It In",50,80,Font3)
    #Right Choice
    game.drawText("Give It In",930,80,Font3)
    game.update(30)
game.over=False
#>
#THE TEACHER COLLECTS HW
while not game.over and hw:
    game.processInput()
    bk2.draw()
    Education=("7th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            w=False
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            Age+=1
            w=False
            game.over=True
    #Decision
    game.drawText("The Teacher Collects HW",350,30,Font2)
    #Choices
    #Left Choice
    game.drawText("Say 'I Lost It'",50,80,Font3)
    #Right Choice
    game.drawText("Say You Did Not Do it",930,80,Font3)
    game.update(30)
game.over=False
#>Age:13
#YOUR PARENTS WANT TO TALK TO YOU
while not game.over and not w:
    game.processInput()
    bk2.draw()
    Education=("8th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            game.over=True
            h=False
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice 2
            Age+=1
            n=True
            game.over=True
    #Decision
    game.drawText("Your Parents Want to Talk to You",130,30,Font2)
    #Choices
    #Left Choice
    game.drawText("Ask Them What About",50,80,Font3)
    #Right Choice
    game.drawText("Yell at Them",1000,80,Font3)
    game.update(30)
game.over=False
#>
#YOUR PARENTS ARE PROUD OF YOU
while not game.over and w:
    game.processInput()
    bk2.draw()
    Education=("8th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            game.over=True
            h=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice 2
            h=True
            game.over=True
    #Decision
    game.drawText("Your Parents Are Proud Of You!",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("Yay!",200,80,Font3)
    #Right Choice
    game.drawText("OK",1000,80,Font3)
    game.update(30)
game.over=False
#>Age:14
#YOUR DAD TAKES YOU CAMPING
while not game.over and h:
    game.processInput()
    bk2.draw()
    Education=("9th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            quality+=10
            game.over=True
            h1=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice
            Age+=1
            quality+=10
            h1=True
            game.over=True
    #Decision
    game.drawText("Your Dad Takes You Fishing",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("OK",200,80,Font3)
    #Right Choice
    game.drawText("Let's Go",1000,80,Font3)
    game.update(30)
game.over=False
#>
#YOUR MOM WANTS TO HELP YOU ACADEMICALLY
while not game.over and not h:
    game.processInput()
    bk2.draw()
    Education=("9th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            game.over=True
            h1=False
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice
            Age+=1
            h2=False
            quality-=10
            game.over=True
    #Decision
    game.drawText("Your Mom Wants to Help Academically",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("OK",200,80,Font3)
    #Right Choice
    game.drawText("Say 'NO' Loudly",1000,80,Font3)
    game.update(30)
game.over=False
#>
#YOU'VE BEEN OFFERED COCAINE
while not game.over and n:
    game.processInput()
    bk2.draw()
    Education=("9th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            health-=50
            n1=True
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice
            Age+=1
            n2=True
            game.over=True
    #Decision
    game.drawText("You've Been Offered Cocaine",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("'Hell Yeah!'",200,80,Font3)
    #Right Choice
    game.drawText("Deny Politely",1000,80,Font3)
    game.update(30)
game.over=False
#>Age:15
#YOU AND YOUR DAD ARE FISHING AGAIN
while not game.over and h1:
    game.processInput()
    bk2.draw()
    Education=("10th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            carp=True
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice
            Age+=1
            salmon=True
            game.over=True
    #Decision
    game.drawText("You And Your Dad Are Fishing Again",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("Try for Carp",200,80,Font3)
    #Right Choice
    game.drawText("Try for Salmon",1000,80,Font3)
    game.update(30)
game.over=False
#>
#YOU'VE ENCOUNTERED A WILD BEAR
while not game.over and not h1:
    game.processInput()
    bk2.draw()
    Education=("10th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            dead1=True
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice
            Age+=1
            dead2=True
            game.over=True
    #Decision
    game.drawText("You Encountered a Wild Bear",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("Run",200,80,Font3)
    #Right Choice
    game.drawText("Try To Kill It",1000,80,Font3)
    game.update(30)
game.over=False
#>
#DEAD
#DEAD
#DEAD
#ONE
while not game.over and dead1:
    game.processInput()
    black.draw()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            gameagain=True
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice
            game.quit=True
    #Decision
    game.drawText("You Have Died",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("Try Again",200,80,Font3)
    #Right Choice
    game.drawText("Quit Game",1000,80,Font3)
    game.update(30)
game.over=False
#>
#DEAD
#DEAD
#DEAD
#TWO
while not game.over and dead2:
    game.processInput()
    bk2.draw()
    Education=("9th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            quality-=50
            n1=True
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice
            Age+=1
            quality-=20
            health-=20
            n2=True
            game.over=True
    #Decision
    game.drawText("Your Dad Died",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("...",200,80,Font3)
    #Right Choice
    game.drawText("Ask Your Friends For Drugs",1000,80,Font3)
    game.update(30)
game.over=False
while not game.over and n1:
    game.processInput()
    bk2.draw()
    Education=("10th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            n1=True
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice
            Age+=1
            n2=True
            game.over=True
    #Decision
    game.drawText("You've Been Offered Cocaine",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("'Hell Yeah!'",200,80,Font3)
    #Right Choice
    game.drawText("Deny Politely",1000,80,Font3)
    game.update(30)
game.over=False
while not game.over and n2:
    game.processInput()
    bk2.draw()
    Education=("10th Grade")
    #Stats
    game.drawText("Age: "+str(Age),1000,10,Font1)
    game.drawText("Health: "+str(Health),400,200,Font1)
    game.drawText("Quality of Life: "+str(Quality),400,300,Font1)
    game.drawText("Financial Status: "+str(Financial),400,400,Font1)
    game.drawText("Education: "+str(Education),400,500,Font1)
    game.drawText("Job: "+str(Job),400,600,Font1)
    #Stats Change
    stats.start()
    #Doors
    for index in range(1):
        #Choice 1 Door
        doors_l[index].draw()
        if mouse.LeftClick and doors_l[index].collidedWith(mouse):
            #Outcome Choice 1
            Age+=1
            n1=True
            game.over=True
    for index in range(1):
        #Choice 2 Door
        doors_r[index].draw()
        if mouse.LeftClick and doors_r[index].collidedWith(mouse):
            #Outcome Choice
            Age+=1
            n2=True
            game.over=True
    #Decision
    game.drawText("You've Been Offered Cocaine",250,30,Font2)
    #Choices
    #Left Choice
    game.drawText("'Hell Yeah!'",200,80,Font3)
    #Right Choice
    game.drawText("Deny Politely",1000,80,Font3)
    game.update(30)
game.over=False
game.quit()
