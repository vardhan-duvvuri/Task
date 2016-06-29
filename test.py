# Design a list in python which accepts only the specified data type(s)
# If any other data type except specified then raise an error
# Perform the operations on it similar to list operations


class MyList():
    """
        A List that accepts the datatype(s) from the user.
        It will accept the data of the specified datatype which
        is set from the user, if any other come it will raise an error.
        It allows the user to perform all the operations of list.
    """
    # Class variable to accept what types of data should be accepted
    datatype = []
    # Constructor method

    def __init__(self):
        self.data_list = []
    # Class Method to set the datatype variable to the user specifivation
    @classmethod
    def acceptonly(cls, user_datatype):
        """
        Method which accepts a datatype as string or list of datatypes as
        tuple

        :param user_datatype: string or tuple (type of the elements to be accepted)
        :return: None
        """
        # If only one datatype passed
        if type(user_datatype) == str:
            MyList.datatype.append(user_datatype)
        # If multiple datatypes passed
        elif type(user_datatype) == tuple:
            for dtype in user_datatype:
                MyList.datatype.append(dtype)

    # Instance Method to append the element to list
    def append(self,element):
        """
        Works similar list append() method
        :param element: of any datatype
        :return: None if the element is of the datatype which is allowed
        :raises exception if the type of element is other than allowed datatypes
        """
        # Check the element is of allowed datatype, if yes then append to list
        if element.__class__.__name__ in MyList.datatype:
            self.data_list.append(element)
        # Raise exception if the element is of different datatype which is not allowed
        else:
            raise Exception("Only {} datatype allowed.".format(MyList.datatype))

    # Instance Method to insert element
    def insert(self,index, element):
        """
        Works similar to list insert() method
        :param index: the index in which new element to be inserted
        :param element: the element to insert into list
        :return: None if the element is of the datatype which is allowed
        :raises exception if the type of element is other than allowed datatypes
        """
        # Check the element is of allowed datatypes, if yes then insert into the specified index
        if element.__class__.__name__ in MyList.datatype:
            self.data_list.insert(index,element)
        # Raise exception if the element is of different datatype which is not allowed
        else:
            raise Exception("Only {} datatype allowed.".format(MyList.datatype))

    # Instance method to extend the list with new list
    def extend(self,element_list):
        """
        Works similar to list insert() method
        :param element_list: list of elements to insert into list
        :return: None if the elements in the list is of the datatype which is allowed
        :raises exception if the type of any element in the list is other than allowed datatypes
        """
        # Loop through all the elements in the list
        for element in element_list:
            # If the element is of the allowed data type insert
            if element.__class__.__name__ in MyList.datatype:
                self.data_list.append(element)
            # else raise exception
            else:
                raise Exception("Only {} datatype allowed.".format(MyList.datatype))

    # Instance method to pop the element
    def pop(self):
        """
        Works similar to list pop() method.
        Removes the most recent element from the list
        :return: The removed/ popped element
        """
        return self.data_list.pop()

    # Instance method to display the list elements
    def show(self):
        """
        Returns the final list
        :return: list of elements of same datatype
        """
        return self.data_list

if __name__ == "__main__":
    # Specify the which datatypes should be allowed
    MyList.acceptonly(("int","float"))
    # create a new list
    newlist = MyList()
    # append an integer to list
    newlist.append(10)
    # append a float value to list
    newlist.append(10.5)
    # extends the list with another list contains allowed datatypes
    newlist.extend([20,20.5])
    # insert the new int element in the 0 th index
    newlist.insert(0,1)
    # Rempve tje most recent element from the list
    newlist.pop()
    # Display all the elements in the list
    print(newlist.show())
    # Try to add string variable to list prodecues error
    newlist.append(newlist.extend([20,20.5,"str"]))
