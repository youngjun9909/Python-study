import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import axios from 'axios';

function App() {

  const [ reqData, setReqData ] = useState({
    title: "",
    img: null
  });

  const handleOnChange = (e) => {

    if(["img"].includes(e.target.name)){
      const files = Array.from(e.target.files)
      console.log(files[0]);
      setReqData(prev => ({
        ...prev,
        [e.target.name]: files[0]
      }))
      return;
    }
    setReqData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }))
  }

  const handleSubmit = () => {
    const formData = new FormData();
    Object.entries(reqData).forEach(entry => {
      const [key, value] = entry;

      if(!!value) {
        formData.append(key, value)
      }
    })

    for( const entry of formData.entries()){
      console.log(entry);
    }

    axios.post("http://localhost:8080/api/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      }
    }). then(response => {
      console.log(response);
    }).catch(error => {
      console.error(error);
    })
  }

  return (
    <div className="App">
      <input type='text' name='title' onChange={handleOnChange} value={reqData.title}/>
      <input type='file' name='img' onChange={handleOnChange}/>
      <button type='submit' onClick={handleSubmit}>전송</button>
    </div> 
  );
}

export default App;
