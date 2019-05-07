class Controller():

  def save(self, task):
    f = open("data.txt", "a+")
    f.write(task + "\r")
    f.close()

  def readAll(self):
    f = open("data.txt", "r")
    if f.mode == "r":
      contents = f.read()
    return contents