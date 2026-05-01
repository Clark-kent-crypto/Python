run=1;
def close(run):
    run=0;
    return 0;

class node:
    def __init__(self,data,next):
        self.data=data;
        self.next=next;
def traverse(Head):
    p=Head;
    
    while(p is not None):
        print(p.data);
        p=p.next;
def isFull(Head):
    p=Head;
    if(p==EOFError):
        print("Stack OverFlow");
        return 1;
def push(Head,data):
    temp=Head;
    var=isFull(Head);
    if(var is not 1):
        p=node(data,temp);
        return p;
    return temp;
def isEmpty(Head):
    p=Head;
    if(p==None):
        print("Stack UnderFlow");
        return 1;
def pop(Head):
    p=Head;
    var=isEmpty(Head);
    if(var is not 1):
        Head=p.next;
        return p.next;
    
    return p;
def save(Head):
    p=Head;
    li=[];
   
    
    while(p is not None):
        li.append(p.data);
        p=p.next;
    FILE=open("text/data.txt","a");
   
    FILE.write(str(li));
    FILE.close();
    return 1;#to make sure the success of svaing can be detected


    





head=node(10,None);

# run=1;
Head=head;
while(run):
    print("=====================================");
    print("                MENU                 ");
    print("=====================================");
    print("1.Exit");
    print("2.Add Number");
    print("3.Delete Number:");
    print("4.Save list")
    # print("4.Show list :");
    try:
        inp=int(input("Enter your choice"));
    except:
        print("Invalid input");
    if(inp==1):
        run=0;
    elif(inp==2):
        num=int(input("Enter the number:"));
        Head=push(Head,num);
    elif(inp==3):
        Head=pop(Head);
    elif(inp==4):
       temp=save(Head)
       if (temp is not 1):
           print("Error in saving");
           
        

    # for i in range(0,10,1):
    #    Head= push(Head,i);
    # Head=pop(Head)

    traverse(Head);
