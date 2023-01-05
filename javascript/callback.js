// your car is broke na and you left it to mechanics to fixed while you go the market for shopping
let carsIsBroken= true;
function callCarOwner(){
    console.log("Hello car owner! car is fixed")
}
const fixCar=(carsIsBroken,callCarOwner)=>{
    if(carsIsBroken === true){
        carsIsBroken=false;
    }
    console.log("IsCarBroken?", carsIsBroken)
    //after the mechanic fixed the car he calls the car owner function
    callCarOwner();
}

fixCar(carsIsBroken,callCarOwner)