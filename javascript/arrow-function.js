//arrow function is called anonymous function like lambda function in python
//arrow function is used to write less code

const addTwoVar = (a,b)=>a+b
console.log(addTwoVar("Sudip"," Shrestha"))
console.log(addTwoVar(2,3))

//arrow function with no parameter
const sayHello=()=>console.log("Hello")
sayHello()
//arrow function with filter,map and reduce
const arr=[2,4,6,8,10]
//prints all number divisbile by 3
console.log(arr.filter((num)=>num%3==0))
//print square of all number
console.log(arr.map((num,index)=>num**2))
//print sum of all number
console.log(arr.reduce((total,num)=>total+num))

//map,foreach
let arr1=[1,2,3,4,5]

let double = arr1.forEach((num)=>num*2)
console.log(double)

let doubled = arr1.map((num)=>num*2)
console.log(doubled)
