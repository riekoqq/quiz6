import React, {useEffect, useState} from 'react'
import { Link, useParams} from 'react-router-dom'
import {Row, Col, Image, ListGroup, Button, Card} from 'react-bootstrap'
import Rating from '../components/Rating'
import axios from 'axios'

function DrugScreen() {
    const { id } = useParams()

    const [drug, setDrug] = useState({})

    useEffect(() => {
        async function fetchDrug() {
            const {data} = await axios.get(`/api/drugs/${id}`)
            setDrug(data)
        }
        fetchDrug()
    }, [])
  return (
    <div>
        <Row>
            <Col md={6}>
                <Image src={drug.image} alt={drug.name} fluid />
            </Col>
            <Col md={3}>
                <ListGroup variant='flush'>
                    <ListGroup.Item>
                        <h3>{drug.name}</h3>
                    </ListGroup.Item>
                    <ListGroup.Item>
                        <Rating value={drug.rating} text={`${drug.numReviews} reviews`} color={'#f8e825'}/>
                    </ListGroup.Item>
                    <ListGroup.Item>
                        Price: <strong>₱{drug.price}</strong>    
                    </ListGroup.Item>
                </ListGroup>
            </Col>
        </Row>
        <Link to='/' className='btn btn-light my-3'>Go Back</Link>
    </div>
  )
}

export default DrugScreen
