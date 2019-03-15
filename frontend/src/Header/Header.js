import React, { Component } from 'react';
import {Navbar, NavbarBrand} from 'reactstrap';

class Header extends Component {
  render() {
    return (
      <div className='mb-3'>
        <Navbar color="light" light expand="md">
            <NavbarBrand href="/">HackerTrend</NavbarBrand>
          </Navbar>
      </div>
    );
  }
}

export default Header;