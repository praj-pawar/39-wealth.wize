import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState({});
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
      fetch("/data")
          .then(res => res.json())
          .then(data => {
              setData(data);
              setIsLoading(false);
          })
          .catch(error => console.error('Error:', error));;
  }, []);

  if (isLoading) {
      return <div>Loading...</div>;
  }

  return (
      <div className="App">
          <p>{data.name}</p>
          <p>{data.age}</p>
          <p>{data.date}</p>
          <p>{data.programming}</p>
      </div>
  );
}

export default App;
