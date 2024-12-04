import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import axios from 'axios';

function App() {

  const [member, setMember] = useState({
    memberId: 0,
    name: '',
    profileImgPath: []
  });

  const [ reqData, setReqData ] = useState({
    title: "",
    img: null
  });

  const handleOnChange = (e) => {

    if(["img"].includes(e.target.name)){
      const files = Array.from(e.target.files)
      console.log(files);
      setReqData(prev => ({
        ...prev,
        [e.target.name]: files
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
        if(key === "img") {
          for(const file of value) {
            formData.append(key, file);
          }
          return;
        }
        formData.append(key, value);
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
      const memberId = response.data.memberId;
      axios.get(`http://localhost:8080/api/member/${memberId}`)
      .then(response => {
        setMember({
          memberId: response.data.memberId,
          name: response.data.name,
          profileImgPath: response.data.profileImgPath.split(",")
        })
      }).catch(error => {
        console.error(error);
      })
    }).catch(error => {
      console.error(error);
    })
  }

  return (
    <div className="App">
      <div>
        <label>이름: </label>
        <input type='text' name='title' onChange={handleOnChange} value={reqData.title}/>
      </div>
      <div>
        <input type='file' name='img' multiple onChange={handleOnChange}/>
      </div>
      <button type='submit' onClick={handleSubmit}>전송</button>

      <div>
        <h1>가입된 회원 정보</h1>
        <div>
          memberId: {member.memberId}
        </div>
        <div>
          name: {member.name}
        </div>
        {member.profileImgPath.map(img => 
          <div>
          <img src={`http://localhost:8080/image/${img}`} />
        </div>
        )
        }
      </div>

    </div> 
  );
}

export default App;
