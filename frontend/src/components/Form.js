
import React, { useState, useEffect } from 'react'
import APIService from './APIService';

function Form(props) {
    const [title, setTitle] = useState('');
    const [body, setBody] = useState('')

    useEffect(() => {
        setTitle(props.article.title)
        setBody(props.article.body)
    },[props.article])

    const updateArticle = () => {
        APIService.UpdateArticle(props.article.id, {title, body})
        .then(resp => props.updatedData(resp))
        .catch(error => console.log(error))
    }

    const insertArticle = () => {
        APIService.InsertArticle({title, body})
        .then(resp => props.insertedArticle(resp))
        .catch(error => console.log(error))
    }

  return (
    <div>
        {props.article ? (
            <div className ="mb-3">
                <label htmlFor='title' className='form-label'>Title</label>
                <input 
                type='text'
                className='form-control'
                value = {title}
                placeholder='please enter Title'
                onChange={(e) => setTitle(e.target.value)}
                />

                <label htmlFor='body' className='form-label'>Body</label>
                <textarea 
                rows="5"
                className='form-control'
                value = {body}
                placeholder='please enter body'
                onChange={(e) => setBody(e.target.value)}
                />

                {
                    props.article.id ?
                    <button className='btn btn-success mt-3' onClick={updateArticle}>Update</button> 
                    :
                    <button className='btn btn-success mt-3' onClick={insertArticle}>Insert</button>
                }

                
            </div>

        ) : null}
    </div>
  )
}

export default Form