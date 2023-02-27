function Card(name, adress, workphone, homephone, email) {
  this.name = name;
  this.adress = adress;
  this.workphone = workphone;
  this.homephone = homephone;
  this.email = email;
  this.PrintCard = PrintCard;
}

function PrintCard() {
  line1 = "Name: " + this.name + "<br>\n";
  line2 = "Address: " + this.adress + "<br>\n";
  line3 = "Workphone: " + this.workphone + "<br>\n";
  line4 = "Homephone: " + this.homephone + "<hr>\n";
  line5 = "email: " + this.email + "<br>\n";
  document.write(line1, line2, line3, line4, line5);
}
tom = new Card("Tom Jones", "123 Elm Street", "555-1234", "555-9876", "fdssd@gmail.com");
holmes = new Card("Shelock Holmes", "221 Baker Street", "555-2345", "555-3456", "NizarH@live.nl");
sue = new Card("Sue Suthers", "123 Elm Street", "555-1234", "555-9876", "Madara@hotmail.com");
phred = new Card("Phred Madsen", "233 Oak Lane", "555-2222", "555-4444", "Kinker@live.com");
henry = new Card("Henry Tillman", "233 Walnut Circle", "555-1299", "555-1344", "Luffy_Strawhat@outlook.com");
tom.PrintCard();
holmes.PrintCard();
sue.PrintCard();
phred.PrintCard();
henry.PrintCard();
