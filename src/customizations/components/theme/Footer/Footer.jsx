/**
 * Footer component.
 * @module components/theme/Footer/Footer
 */

import React from 'react';
import { Container, List, Segment } from 'semantic-ui-react';
import { Link } from 'react-router-dom';
import { FormattedMessage, defineMessages, injectIntl } from 'react-intl';
import IconFbook from '../../../../../theme/assets/facebook.svg';
import IconTwit from '../../../../../theme/assets/twitter.svg';
import IconInst from '../../../../../theme/assets/instagram.svg';
import IconMail from '../../../../../theme/assets/mail.svg';

const messages = defineMessages({
  copyright: {
    id: 'Copyright',
    defaultMessage: 'Copyright',
  },
});

/**
 * Component to display the footer.
 * @function Footer
 * @param {Object} intl Intl object
 * @returns {string} Markup of the component
 */
const Footer = ({ intl }) => (
  <Segment
    role="contentinfo"
    vertical
    padded
    inverted
    color="white"
    textAlign="center"
    id="footer"
  >
    <Container>
      <Segment basic inverted color="white" className="discreet">
        <div className="footer-row1">
          <a href="#">
            <img className="sm-icon" src={IconFbook} alt="facebook icon" />
          </a>
          <a href="#">
            <img className="sm-icon" src={IconTwit} alt="twitter icon" />
          </a>
          <a href="#">
            <img className="sm-icon" src={IconInst} alt="instagram icon" />
          </a>
          <a href="#">
            <img className="sm-icon" src={IconMail} alt="e-mail icon" />
          </a>
        </div>
        <div className="footer-row2">
          <h4>Twenty Twenty-One</h4>
          <span className="footer-text">
            Proudly powered by{' '}
            <a className="link-1" href="#">
              kitconcept.
            </a>
          </span>
        </div>
      </Segment>
    </Container>
  </Segment>
);

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
Footer.propTypes = {
  /**
   * i18n object
   */
};

export default injectIntl(Footer);
