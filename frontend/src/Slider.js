import React from 'react'
import { Form, Button, Col, Row } from 'react-bootstrap';
import RangeSlider from "react-bootstrap-range-slider";

export const SliderWithInputFormControl = () => {

    const [ value, setValue ] = React.useState(25);
  
    return (
      <Form>
        <Form.Group as={Row}>
          <Col xs="8">
            <RangeSlider
              value={value}
              onChange={e => setValue(e.target.value)}
              style={{width:"350px"}}
            />
          </Col>
          {/* <Col>
            <Form.Control style={{width:'10px'}} value={value}/>
          </Col> */}
        </Form.Group>
      </Form>
    );
  
  };