// function rand(num) {
//   return Math.floor(Math.random() * num) + 1;
// }

total = 0;
for (i = 1; i <= 5000; i++) {
  num = Math.random();
  total += num;

  if (i % 1000 == 0)
    document.write("Generated " + i + " numbers...<br>");
}

average = total / 5000;
average = Math.round(average * 1000) / 1000;
document.write("<H2>Average of 5000 numbers: " + average + "</H2>");

with (lastname) {
  window.alert("length of last name: " + length);
  capname = toUpperCase();
}

holiday.setFullYear(2004);