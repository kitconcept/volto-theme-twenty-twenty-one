/**
 * Header component.
 * @module components/theme/Header/Header
 */

import React, { Component } from 'react';
import { Container, Segment } from 'semantic-ui-react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import {
  Anontools,
  LanguageSelector,
  Logo,
  Navigation,
  SearchWidget,
} from '@plone/volto/components';

/**
 * Header component class.
 * @class Header
 * @extends Component
 */
class Header extends Component {
  /**
   * Property types.
   * @property {Object} propTypes Property types.
   * @static
   */
  static propTypes = {
    token: PropTypes.string,
    pathname: PropTypes.string.isRequired,
  };

  /**
   * Default properties.
   * @property {Object} defaultProps Default properties.
   * @static
   */
  static defaultProps = {
    token: null,
  };

  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */
  render() {
    return (
      <Segment basic className="header-wrapper" role="banner">
        <Container>
          <div className="header-row1">
            <logo>Twenty Twenty-One</logo>
            <ul className="link-list">
              <li>
                <a className="active-site page-link" href="#">
                  Home
                </a>
                <a className="page-link" href="#">
                  About
                </a>
                <a className="page-link" href="#">
                  Blog
                </a>
                <a className="page-link" href="#">
                  Contact
                </a>
              </li>
            </ul>
          </div>
          <div className="header-row2">
            <p>Twenty Twenty-One! Create your own inovative slogan.</p>
          </div>
        </Container>
      </Segment>
    );
  }
}

export default connect((state) => ({
  token: state.userSession.token,
}))(Header);
