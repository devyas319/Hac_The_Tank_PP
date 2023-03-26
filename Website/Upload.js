import React, { useState } from 'react';
import axios from 'axios';
import './App.css'
import foot2 from './images/foot_2.jpg'

function Upload() {
  const [output, setOutput] = useState('');
  const [leftFootImage, setLeftFootImage] = useState(null);
  const [rightFootImage, setRightFootImage] = useState(null);

  const handleLeftFootImageChange = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = () => {
      setLeftFootImage(reader.result);
    };
    reader.readAsDataURL(file);
  };

  const handleRightFootImageChange = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = () => {
      setRightFootImage(reader.result);
    };
    reader.readAsDataURL(file);
  };

  const handlePredictionClick = () => {
    const formData = new FormData();
    formData.append('leftFootImage', leftFootImage);
    formData.append('rightFootImage', rightFootImage);
    const config = {
      headers: { 'content-type': 'multipart/form-data' }
    };
    axios.post('http://localhost:5000/predict', formData, config)
      .then(response => {
        setOutput(response.data.result);
      })
      .catch(error => {
        console.error('Error predicting output:', error);
      });
  };

  return (
    <div className='upload'>
      <div className='foot2_img'>
        <img src={foot2} alt='foot2' className='foot2'/>
      </div>
      <label className='custom-input' htmlFor='leftFootImage'>Upload Your Left Foot Image</label>
      <input type='file' id='leftFootImage' accept='image/*' onChange={handleLeftFootImageChange} className='input' />
      {leftFootImage && <img src={leftFootImage} alt='Left Foot' style={{ maxWidth: '100%', maxHeight: '100%', marginLeft: '40px', marginTop: '10px' }} />}
      <label className='custom-input' htmlFor='rightFootImage'>Upload Your Right Foot Image</label>
      <input type='file' id='rightFootImage' accept='image/*' onChange={handleRightFootImageChange} className='input' />
      {rightFootImage && <img src={rightFootImage} alt='Right Foot' style={{ maxWidth: '100%', maxHeight: '100%', marginLeft: '40px', marginTop: '10px' }} />}
      <button className='predict-button' onClick={handlePredictionClick}>Predict Output</button>
      {/* Display the predicted output */}
      {output && <p>The predicted output is: {output}</p>}
      {/* Display the uploaded images */}
      {leftFootImage && (
        <div>
          <h3>Left Foot Image</h3>
          <img src={leftFootImage} alt='Left Foot' style={{ maxWidth: '300px', maxHeight: '300px' }} />
        </div>
      )}
      {rightFootImage && (
        <div>
          <h3>Right Foot Image</h3>
          <img src={rightFootImage} alt='Right Foot' style={{ maxWidth: '300px', maxHeight: '300px' }} />
        </div>
      )}
    </div>
  );
}

export default Upload;
