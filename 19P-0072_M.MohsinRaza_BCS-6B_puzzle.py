#---------------- Assignment No. 1--------------#
import copy
import time

class puzzle:
    def __init__(self,initial_state,goal_state):
        self.parent=None
        self.first_child=None
        self.second_child=None
        self.third_child=None
        self.fourth_child=None
        self.state=initial_state
        self.goal=goal_state
        
    def get(self):
        # print('Initail_state:',*self.state,sep='\n')
        # print('Goal: ',*self.goal,sep='\n' )
        if self == None:
            return
        print(*self.state,sep='\n')
        print('\n')

        if self.first_child is not None:
            self.first_child.get()
        if self.second_child is not None:    
            self.second_child.get()
            # print(self.state)
        if self.third_child is not None:
            self.third_child.get()
            # print(self.state)
        if self.fourth_child is not None:
            self.fourth_child.get()
        # print(self.state)
        
    #----- convert 2d list of state into 1-D space----#
    def list_of_2d_state(self,state):

        list_of_state=[]
        for i in state:
            row=i
            for j in range(4):
                list_of_state.append(row[j])
        
        return list_of_state
    
    #------ commmented code will tell key as tile no. and value will tell how many tiles are less than that tile----#
    def pirority(self,initial_state_list_1d):
        count=0
        result={}
        for item in initial_state_list_1d:
            index=initial_state_list_1d.index(item)

            for i in range(index+1,len(initial_state_list_1d)):
    #             print(item,initial_state_list_1d[i])
                if item != ' ' and initial_state_list_1d[i] != ' ':                   
                    if item > initial_state_list_1d[i]:

                        count=count+1
    #                     result[item]=count
    #         count=0
    #     print('r :',result)
    #     return result
        return count          
            

        
    def is_reachable(self):
        count=0

        index_of_initial_state=0
        #---- Converts to 1 d array to -----#
        initial_state_list_1d=self.list_of_2d_state(self.state)
#         print('1d:',initial_state_list_1d)

        goal_state_list_1d=self.list_of_2d_state(self.goal)
        #---- Stores a piroirty of given state------#
        
        pirority_of_initinal_state=self.pirority(initial_state_list_1d)
        pirority_of_goal_state=self.pirority(goal_state_list_1d)
        print('pirority_of_initinal_state: ',pirority_of_initinal_state)
        print('pirority_of_goal_state: ',pirority_of_goal_state)
        if pirority_of_goal_state %2 ==0 and pirority_of_initinal_state %2 ==0 :
            print('Solution is possible ....')
            return True
        if pirority_of_goal_state %2 !=0 and pirority_of_initinal_state %2 !=0 :    
            print('Solution is possible ....')
            return True
        else:
            print('Solution not possible...')
            return False
    

    def index_of_free_space(self):
        index_of_free_space_x=None
        index_of_free_space_y=None
        for i in range(3):
            for j in range(4):
                if self.state[i][j]==' ':
                    index_of_free_space_x=i
                    index_of_free_space_y=j
        return index_of_free_space_x,index_of_free_space_y

    #------------ First Child-------------------#
    #------------ Move Down ----------------------#
    def first_child_state(self):
        # print('In:',*self.state,sep='\n',end='\n')
        index_of_free_space_x,index_of_free_space_y=self.index_of_free_space()
        
        # print(index_of_free_space_x,index_of_free_space_y)
        
        plus_x=index_of_free_space_x+1
        
        

        if (plus_x < 3 and plus_x > 0) and (index_of_free_space_y <4):
            tmp_state= copy.deepcopy(self.state)
            tmp_state[index_of_free_space_x][index_of_free_space_y] = tmp_state[plus_x][index_of_free_space_y]
            tmp_state[plus_x][index_of_free_space_y]=' '
            self.first_child = puzzle(tmp_state,self.goal)
            self.first_child.parent= self
            # print('child: ',*self.first_child.state,sep='\n')
            # print('\n')
            # print('state:',self.state)


    #----------- Second Child-------------#
    #--------- Move Right ----------------#
    def second_child_state(self):
        # print('In:',*self.state,sep='\n')
        index_of_free_space_x,index_of_free_space_y=self.index_of_free_space()
        
        # print(index_of_free_space_x,index_of_free_space_y)
        
        # plus_x=index_of_free_space_x+1
        plus_y=index_of_free_space_y+1
        
    
        if index_of_free_space_x < 3 and  (plus_y <4 and plus_y > 0):
            tmp_state= copy.deepcopy(self.state)
            tmp_state[index_of_free_space_x][index_of_free_space_y] = tmp_state[index_of_free_space_x][plus_y]
            tmp_state[index_of_free_space_x][plus_y] =' '
            self.second_child = puzzle(tmp_state,self.goal)
            self.second_child.parent=self
            # print('second child: ',*self.second_child.state,sep='\n')
            # print('\n')

    #------------ Third Child-------------#
    #------------ Move Up -------------#
    def third_child_state(self):
        # print('In:',*self.state,sep='\n')
        index_of_free_space_x,index_of_free_space_y=self.index_of_free_space()
        
        
        minus_x=index_of_free_space_x-1
        
        # print(minus_x,index_of_free_space_y)
        if (minus_x < 3 and minus_x >= 0) and index_of_free_space_y <4:
            tmp_state= copy.deepcopy(self.state)
            tmp_state[index_of_free_space_x][index_of_free_space_y] = tmp_state[minus_x][index_of_free_space_y]
            tmp_state[minus_x][index_of_free_space_y]=' '
            self.third_child = puzzle(tmp_state,self.goal)
            self.third_child.parent=self
            # print('third child: ',*self.third_child.state,sep='\n')
            # print('\n')

    #-------------- Fourth Child ------------#
    #-------------- Move Left----------------#
    def fourth_child_state(self):
        # print('In:',*self.state,sep='\n')
        index_of_free_space_x,index_of_free_space_y=self.index_of_free_space()
        
        
        minus_y=index_of_free_space_y-1
        
        
        if index_of_free_space_x < 3 and  (minus_y <4 and minus_y >= 0):
            tmp_state= copy.deepcopy(self.state)
            tmp_state[index_of_free_space_x][index_of_free_space_y] = tmp_state[index_of_free_space_x][minus_y]
            tmp_state[index_of_free_space_x][minus_y] =' '
            self.fourth_child = puzzle(tmp_state,self.goal)
            self.fourth_child.parent=self
            # print('fourth child: ',*self.fourth_child.state,sep='\n')
            # print('\n')
    #--------------------------------------------------------------------------#

    def make_tree(self):
        # while self.state != self.goal:
            if self == None:
                return
            if self.first_child is not None:
                self.first_child.make_tree()
            if self.first_child is None:    
                self.first_child_state()

            if self.second_child is not None:
                self.second_child.make_tree()
            if self.second_child is None:
                self.second_child_state()

            if self.third_child is not None:
                self.third_child.make_tree()
            if self.third_child is None:
                self.third_child_state()

            if self.fourth_child is not None:
                self.fourth_child.make_tree()
            if self.fourth_child is None:
                self.fourth_child_state()
            # print('-----Level Completed-----')

    def is_already_explored(self,state,list):
        flage = True
        for items in list:
            if state == items.state:
                flage = False
                return flage
        return flage

    def reverse(self,Node):
        path=[]
        while Node is not None:
            
            path.append(Node.state)
            Node=Node.parent
        path.reverse()
        print('-----path found-----')
        print(*path,sep='\n')
        # print(item.state for item in path)

    def iterative_deeping(self):
        frontier=[]    
        explored_states=[]
        
        #------ root is appending------#
        frontier.append(self)
        
            
        #-----  if frontiers is empty then no sol ----#
        while len(frontier) !=0 :
            f1=[]
            e1=[]
            for f in frontier:
                f1.append(f.state)
            print('frontier values:',*f1,sep='\n')
            
            for e in explored_states:
                e1.append(e.state)

            print('\n')    
            print('explored states:',*e1,sep='\n')
            print('\n')
            
            
            # remove a node from frontier
            tmp_node = frontier.pop()
            print('poping element:',*tmp_node.state,sep='\n')


            # apply goal test
            print('Applying goal test','\n')
            if tmp_node.state == self.goal:
                self.reverse(tmp_node)
                print('--------------Found------------------------')
                return True
            # add node to explored state
            explored_states.append(tmp_node)
            
            # Expande node  add resulting nodes  to frontier
            # if they aren't in ecplored set
            print('Expanding Nodes','\n')
            if tmp_node.first_child != None:
                if self.is_already_explored(tmp_node.first_child.state,explored_states):
                    frontier.append(tmp_node.first_child)

            if tmp_node.second_child != None:
                if self.is_already_explored(tmp_node.second_child.state,explored_states):
                    frontier.append(tmp_node.second_child)

            if tmp_node.third_child != None:
                if self.is_already_explored(tmp_node.third_child.state,explored_states):
                    frontier.append(tmp_node.third_child)
        
                

            if tmp_node.fourth_child != None:
                if self.is_already_explored(tmp_node.fourth_child.state,explored_states):
                    frontier.append(tmp_node.fourth_child)

            print('---------------------')
            
        print('No solution exist :')

    def level(self):
        # while solution not exist:
        i=0
        self.make_tree()
        while self.iterative_deeping() is not True :
            self.make_tree()

            i+=1
            
            
i=[[' ',9,8,1],[4,5,6,7],[2,3,10,11]]
g=[[4, 9, 8, 1],[2, 5, 6, 7],[' ', 3, 10, 11]]
p=puzzle(i,g)
if p.is_reachable():
    l=1
    while l >0:
        # time.sleep(2)
        # print('Adding Level :',l)
        p.make_tree()
        if p.iterative_deeping():
            break
        l=l+1

