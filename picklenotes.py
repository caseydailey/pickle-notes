#see docs: https://docs.python.org/3/library/pickle.html
import pickle

class Notes:
  '''
  defines properties and methods for a CLI to record user input, 
  serialize it, write it to a file, and retrieve it.

  properties:
    all_notes-- (list) containing previous user input (notes)

  methods:
    list_notes(self)
    prompt(self)
    serialize(self)
    deserialize(self)

  '''

  #if there are notes, 
  #get them them, deserialize them (see deserialize() method below)
  #and assign them to the empty set up for them.
  #if none exist, pass. (notes will be written to the list when entered by user)
  def __init__(self):
    self.all_notes = []
    try:
      self.all_notes = self.deserialize()
    except FileNotFoundError:
      pass

  #invoke when input = 'ls'
  #iterates through all_notes list, returning and 'enumerate object', which is printed like this
  #0: first note
  #1: second note 
  def list_notes(self):
    for key,note in enumerate(self.all_notes):
      print(str(key) + ": " + note)

  #handles user input
  def prompt(self):
    '''responds conditionaly to user input
       
       arg: self (instance of app)
       returns: 1 of 4 actions based on user input
    '''

    #prompt user for input
    note = input("Enter quick note > ")

    #if user inputs 'ls' list_notes
    if note == "ls":
      self.list_notes()

    # 'rm' will list notes, ask which to delete, 
    # and pass that to delete, converted to integer represent a key
    # in all_notes dictionary
    elif note == "rm":
      self.list_notes()
      deleted = input("Which one? > ")
      del(self.all_notes[int(deleted)])

    #else if user input is not 'quit', 
    #it must be a note
    #in this case append input (note) to the notes list and serialize
    elif note != "quit":
      self.all_notes.append(note)
      self.serialize()

    #bring back the prompt as long as they haven't typed 'quit'
    if note != "quit": self.prompt()

  #open notes and write, in 'binary' by passing all_notes list to 
  #pickle's dump method https://docs.python.org/3/library/pickle.html
  def serialize(self):
    with open(notes.txt, wb+) as f:
      pickle.dump(self.all_notes, f)


  #try to open notes.txt, read the binary using pickle's load method
  #assign the resulting value to all_notes (a list)
  def deserialize(self):
    try:
      with open(notes.txt, rb+) as f:
        self.all_notes = pickle.load(f)
    #https://docs.python.org/3.6/library/exceptions.html
    #EOFError means the file was read, but there was nothing in it.
    except EOFError:
      pass
    #return a list of the notes
    return self.all_notes





