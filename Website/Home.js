import React from 'react'
import { Link } from 'react-router-dom'
import foot from './images/foot.png'
import './App.css'
import ImgBg from './images/img_bg.png'

function Home() {
  return (
    <div className='home'> 
        <div className='foot_img'>
            <img src={foot} alt='foot' className='foot'/>
        </div>
        <h1 className='home_txt'>Get back on your feet with Your Foot Doctor</h1>
        <Link to='/upload'><button className='btn'>Upload your foot images</button></Link>
        <span className='span'>OR</span>
        <Link to='/capture'><button className='btn'>Capture your foot images</button></Link>       
    </div>
  )
}

export default Home
