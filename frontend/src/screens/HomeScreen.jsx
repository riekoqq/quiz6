import React, { useState, useEffect } from 'react'
import Drug from '../components/Drug.jsx'
import axios from 'axios'
import { Row, Col } from 'react-bootstrap'

function Homescreen() {
  const [drugs, setDrugs] = useState([])

  useEffect(() => {
    async function fetchDrugs() {
      const {data} = await axios.get('/api/drugs/')
      setDrugs(data)
    }
    fetchDrugs()
  }, [])

  return (
    <div>
      <h1>Droga ng Bayan</h1>
      <Row>
          {drugs.map((drug) => (
            <Col key={drug._id} sm={12} md={6} lg={4} xl={3}>
              <Drug drug={drug} />
            </Col>
          ))}
      </Row>
    </div>
  )
}

export default Homescreen
