$(document).ready(function(){
  
    function flavor() {
      let selectFlavor = document.getElementById("flavor").value;
      return parseInt(selectFlavor);
    }
    
    function crust() {
      let selectCrust = document.getElementById("crust").value;
      return parseInt(selectCrust);
    }
    function topping() {
      let selectTopping = document.getElementById("topping").value;
      return parseInt(selectTopping);
    }
    function number() {
      let inputNumber = document.getElementById("number").value;
      return parseInt(inputNumber);
    }
  
    function order(flavor,crust, topping, number) {
      this.newFlavor = flavor;
      this.newCrust = crust;
      this.newTopping = topping;
      this.newNumber = number;
    }
  
    let userInput = new order(flavor(),crust(),topping(),number()); 
  
      prompt("enter your email address");
      prompt("enter your phone number");
      prompt("enter your location");
      alert("Your pizza will be delivered to you in an instant and your delivery cost is sh.250.Thank you for choosing us");
  
  
    $("#formgroup")(function(execute) {
    execute.preventDefault();
  });
  });
  
  