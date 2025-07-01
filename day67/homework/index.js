// ობიექტის შექმნა
const student = {
  name: "ბაჩა",
  surname: "ტყემალაძე",
  academy: "goa",
  city: "თბილისი",
  role: "მოსწავლე",
  favColor: "ლურჯი",


  fullName: function () {
    console.log(this.name + " " + this.surname);
  },

  
  showFavColor: function () {
    console.log(this.favColor);
  }
};

console.log(student);
console.log(student.city);


student.fullName();


student.favColor = "წითელი";
console.log(student.favColor);
