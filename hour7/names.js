names = new Array();

i = 0;

do {
  next = window.prompt("Enter the Next Name", "");
  if (next > " ") names[i] = next;
  names.sort();
  i = i + 1;
}
while (next > " ");
document.write("<h2>" + (names.length) + "names entered.</h2>");
// laat de names zien
// <ol> is trouwens orderd list
// <li> is een item van de list
document.write("<ol>");
for (i in names) {
  document.write("<li>" + names[i] + "<br>");
}
document.write("</ol>");

