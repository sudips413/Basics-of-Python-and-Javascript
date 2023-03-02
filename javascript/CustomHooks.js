function useToggle(intialvalue){
    const data = intialvalue;
    function toggle(){
        data = !data;
    }
    return [data, toggle];
}


// use in react component
const [data, toggle] = useToggle(false);
console.log(data); // false
toggle();
console.log(data); // true