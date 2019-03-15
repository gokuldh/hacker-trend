import React from 'react';
import ReactDOM from 'react-dom';
import Stories from './Stories';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<Stories />, div);
  ReactDOM.unmountComponentAtNode(div);
});
