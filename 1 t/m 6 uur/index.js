console.log("Nizar")
nizar = 3
console.log(nizar)

var number = 2
console.log(number)
// var kan door heel je programma door gebruikt worden
let Mohamed = "2 februari"
console.log(Mohamed)
// let 

const pi = 3.14
// kan je nooit veranderen

var a = 1;
var b = 2;
var c = "String";

a = a + 3;
b = b + 7;
c = c + "BLA";


b = a

console.log(a)
console.log(b)
console.log(c)

// declarations
var Anas;
var rick
var MOrty

// assignments 
ANAS = 10;
RIck = "dwcd";
morty = 7077;
// Javascript is hoofdlettergevoelig

var sum = 10 + 10;
console.log(sum)
// hoe je een som kan maken in javascript
var difference = 10 - 3
console.log(difference)
// dit is hoe je min sommen maakt
var product = 10 * 4
console.log(product)
// keersommen
var ourDecimal = 7.

//var mystr = " I am a" double quoted" string inside" double quotes"";
// om dit op te lossen kan je een \ er bij voege
var mystr = " I am a \" double quoted\" string inside \" double quotes";
console.log(mystr)

/***** 
CODE OUTPUT
\' single quote
\" double quote
\\ backslash
\n newline
\r carriage return
\t tab
\b backspace
\f form feed
*****/

var Mytr = "Firstline\n\t\\ SecondLine\nThirdline"
console.log(Mytr)

var bla = "i am first." + "I am second.";
var Mid = "This is the start" + "This is the end";
console.log(bla);

var Ourstr = "Ik ben Nizar. ";
Ourstr += "Aangenaam Nizar, ik ben Joost";
console.log(Ourstr)

// je kan strings ook met variable combineren
var Name = "Ali";
var Str = "Hello, my name is " + Name + ", how are you?";
console.log(Str)

var anAdjective = " awesome";
var Rt = "Rotterdam is";
Rt += anAdjective;
console.log(Rt)

// lengte van een woord kunnen zien met .length
var lastNameLength = 4;
var lastName = "Haddouch";
lastNameLength = lastName.length;
console.log(lastNameLength)

// kunnen zien wat de eerste letter is dat begint bij 0
var firstLetterFirstName = "";
var FirstName = "Nizar";

firstLetterFirstName = FirstName[0];
console.log(firstLetterFirstName)

// een letter veranderen kan niet dus moet je de hele woord veranderen
var String1 = "Jello World";
String1 = "Hello World";
console.log(String1)

// zo kan je de laatste letter vinden zonder te kijken hoeveel letters een woord heeft
var lastNaam = "Haddouch";
var lastLetterOfLastnaam = lastNaam[lastNaam.length - 7];
console.log(lastLetterOfLastnaam)


function wordBlanks(myNoun, myAdjective, myVerb, myAdverb) {
  var result = "";
  result = "The" + " " + myAdjective + " " + myNoun + " " + myVerb + " " + "to the store" + " " + myAdverb
    + "."
  return result;
}
console.log(wordBlanks("dog", "big", "ran", "quikly"));

var myArray = [18, 64, 99];
var myData = myArray[0];
console.log(myData);

var NewArray = [18, 64, 99];
NewArray[0] = 65343;
console.log(NewArray)

var moArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [[10, 11, 12], 13, 14]];

var nArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [[10, 11, 12], 13, 14]];

var nData = nArray[2][1];
console.log(nData);

var kArray = [["John", 23], ["cat", 2]];
kArray.push(["dog", 3])
console.log(kArray)

var olArray = [["John", 23], ["cat", 2]];

var removedFromArray = olArray.pop();
console.log(olArray)

var Ou