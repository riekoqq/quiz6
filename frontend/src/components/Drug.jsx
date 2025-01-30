import React from 'react'
import { Card } from 'react-bootstrap'
import Rating from './Rating'
import { Link } from 'react-router-dom'

function Drug({ drug }) {
  return (
    <Card className='my-3 p-3 rounded'>
      <Link to={`/drug/${drug._id}`}>
        <Card.Img 
          src={drug.image} 
          style={{ width: '100%', height: '200px', objectFit: 'cover' }} 
        />
      </Link>
      <Card.Body>
        <Link to={`/drug/${drug._id}`}>
          <Card.Title as='div'>
            <strong className='text-dark'>{drug.name}</strong>
          </Card.Title>
        </Link>
        <Card.Text as='h3'>₱{drug.price}</Card.Text>
        <Card.Text>
          <Rating value={drug.rating} text={`${drug.numReviews} reviews`} color='#f8e825'/>
        </Card.Text>
      </Card.Body>
    </Card>
  )
}

export default Drug
