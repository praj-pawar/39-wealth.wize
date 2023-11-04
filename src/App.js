import React,{useState,useEffect} from 'react'

function App() {
  const [data,setData]=useState([{}])

  useEffect(() => {
       fetch("/about")
           .then(res => res.json())
           .then(data => setData(data));
   }, []);

  return (
    <div>
         <div className="App">
           <p>{data.name}</p>
           <p>{data.age}</p>
           <p>{data.date}</p>
           <p>{data.programming}</p>
       </div>
    </div>
  )
}

export default App