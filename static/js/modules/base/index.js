/**
 * @license
 * Copyright (c) 2021. CRON LLC. All rights reserved.
 * The copyright notice above does not evidence any actual or
 * intended publication of such source code. The code contains
 * CRON LLC Confidential Proprietary Information.
 */

import MDCIconButtonSheet from '@material/icon-button/dist/mdc.icon-button.css' assert { type: 'css' };
import MDCListSheet from '@material/list/dist/mdc.list.css' assert { type: 'css' };
import { MDCMenu } from '@material/menu';
import { Corner } from '@material/menu-surface';
import MDCMenuSurfaceSheet from '@material/menu-surface/dist/mdc.menu-surface.css' assert { type: 'css' };
import MDCMenuSheet from '@material/menu/dist/mdc.menu.css' assert { type: 'css' };
import { MDCSnackbar } from "@material/snackbar";
import MDCSnackbarSheet from '@material/snackbar/dist/mdc.snackbar.css' assert { type: 'css' };
import MDCButtonSheet from '@material/button/dist/mdc.button.css' assert { type: 'css' };
import sheet from './styles.css' assert { type: 'css' };
import '@/material-icons/action';
import injectSVG from '@/material-icons/utils/injectSVG';

document.adoptedStyleSheets = [
  ...document.adoptedStyleSheets,
  MDCIconButtonSheet,
  MDCListSheet,
  MDCMenuSurfaceSheet,
  MDCMenuSheet,
  MDCSnackbarSheet,
  MDCButtonSheet,
  sheet
];

injectSVG((new URL('./sprite.svg', import.meta.url)).href);

if (document.getElementById('profile-menu')) {
  const profileMenu = new MDCMenu(document.getElementById('profile-menu'));
  const profileMenuButton = document.getElementById('profile-menu-button');

  profileMenu.setAnchorCorner(Corner.BOTTOM_LEFT);

  profileMenuButton.addEventListener('click', () => {
    if (profileMenuButton.dataset.menuIsOpen === 'false') {
      profileMenu.open = true;
      profileMenuButton.dataset.menuIsOpen = 'true';
    }
  });

  profileMenu.menuSurface.listen('MDCMenuSurface:closed', () => {
    profileMenuButton.dataset.menuIsOpen = 'false';
  });
}

/**
 * Class representing a messagesQueue.
 */
class MessagesQueue {
  /**
   * Create a messagesQueue
   */
  constructor() {
    this.messages = []
  }

  /**
   * Add message to queue
   * @param {MDCSnackbar} message
   */
  add(message) {
    this.messages.push(() => {
      message.open();
      message.listen('MDCSnackbar:closed', () => {
        this.messages.shift();
        if (this.messages.length > 0) {
          this.messages[0]();
        }
      })
    });
    if (this.messages.length === 1) {
      this.messages[0]();
    }
  }
}

const messagesQueue = new MessagesQueue();

Array.from(document.querySelectorAll('.message')).forEach((message) => {
  messagesQueue.add(new MDCSnackbar(message));
});

globalThis.sendMessageToSnackbar = function (messageText) {
  const messagesContainer = document.querySelector('.messages');
  messagesContainer.insertAdjacentHTML('beforeend', `
    <div class="mdc-snackbar message">
      <div class="mdc-snackbar__surface">
        <div class="mdc-snackbar__label" role="status" aria-live="polite">
          ${messageText}
        </div>
      </div>
    </div>
  `);

  const messageElement = Array.from(messagesContainer.querySelectorAll('.message')).pop();
  const message = new MDCSnackbar(messageElement);
  messagesQueue.add(message);
};
