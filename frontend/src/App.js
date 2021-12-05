import logo from './logo.svg';
import './App.css';
import { Accordion, InputGroup, FormControl, Image, Navbar, Card,Container, Form, Button, Col, Row } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'
import { width } from 'dom-helpers';
import {SliderWithInputFormControl} from './Slider'
import React from 'react'
import holder from './GoogleMapHolder.jpg'; // Tell webpack this JS file uses this image

function App() {
  return (
    <div className="App">
      <Navbar bg="primary" variant="dark">
        <Navbar.Brand style={{width:'8000px'}}>Elevation Based Navigation</Navbar.Brand>
      </Navbar>
      <body className="App-header" style={{outerHeight:'1000px'}}>
      
       <Container fluid>
         {/* <Row>
         <Col xs={6}>
         <Form>
         <Form.Group className="mb-3" controlId="formBasicEmail">
    <Form.Label>Email address</Form.Label>
    <Form.Control type="email" placeholder="Enter email" />
    <Form.Text className="text-muted">
      We'll never share your email with anyone else.
    </Form.Text>
  </Form.Group>

  <Form.Group className="mb-3" controlId="formBasicPassword">
    <Form.Label>Password</Form.Label>
    <Form.Control type="password" placeholder="Password" style={{width:"200px"}}/>
  </Form.Group>
  <Form.Group className="mb-3" controlId="formBasicCheckbox">
    <Form.Check type="checkbox" label="Check me out" />
  </Form.Group>
  <Button variant="primary" type="submit">
    Submit
  </Button>
</Form>
         </Col>
         <Col style={{width:"30%"}}>
       <Form>
  <Form.Group className="mb-3" controlId="formBasicEmail">
    <Form.Label>Email address</Form.Label>
    <Form.Control type="email" placeholder="Enter email" />
    <Form.Text className="text-muted">
      We'll never share your email with anyone else.
    </Form.Text>
  </Form.Group>

  <Form.Group className="mb-3" controlId="formBasicPassword">
    <Form.Label>Password</Form.Label>
    <Form.Control type="password" placeholder="Password" />
  </Form.Group>
  <Form.Group className="mb-3" controlId="formBasicCheckbox">
    <Form.Check type="checkbox" label="Check me out" />
  </Form.Group>
  <Button variant="primary" type="submit">
    Submit
  </Button>
</Form>
<SliderWithInputFormControl></SliderWithInputFormControl>
</Col>
</Row> */}
<Row>
    <Col xs={7}>
{/* style={{height:"738px", marginRight:'8px', marginTop:'22px', width:"950px"}} */}
{/* <Container> */}
    <Card style={{height:"738px", marginRight:'8px', marginTop:'22px'}} >
  {/* <Card.Body> */}
  <Image src={holder} rounded style={{height:"738px", marginRight:'8px', marginTop:'0px', width:"950px"}} />
  {/* </Card.Body> */}
  </Card>
{/* </Container>     */}
    </Col>
    <Col >
    <Card style={{height:"738px", marginRight:'8px', marginTop:'22px'}}>
  <Card.Body>
  <Form style={{marginLeft:"30px", marginTop:"30px"}}>
  <InputGroup className="mb-3" style={{width:"580px", marginTop:"25px"}}>
    <InputGroup.Text id="basic-addon1">Source</InputGroup.Text>
    <FormControl
      placeholder="Source"
    />
  </InputGroup>
  <Row>
  <InputGroup className="mb-3"  style={{width:"580px"}}>
    <InputGroup.Text id="basic-addon1">Destination</InputGroup.Text>
    <FormControl
      placeholder="Destination"
    />
  </InputGroup>
  </Row>
  <Row style={{fontSize:'20px', marginLeft:'1px', marginTop:"10px"}}>
      Elevation Percentage :

    <Col>
    <SliderWithInputFormControl/>
    </Col>
  </Row>
  

  <Button variant="success" type="submit" style={{marginTop:"10px"}}>
    Generate Map
  </Button>
</Form>
<Accordion style={{marginTop:"15px", width:"340px", marginLeft:"32px", width:"570px"}}>
  <Accordion.Item eventKey="0">
    <Accordion.Header>Click for Elevation Statistics</Accordion.Header>
    <Accordion.Body>
      No Stats Currently!
    </Accordion.Body>
  </Accordion.Item>
</Accordion>
  </Card.Body>
  </Card>
   </Col>
  </Row>
  <Row>
  

  </Row>
       </Container>
      </body>
    </div>
  );
}

export default App;
