import React from 'react';
import { Button, Container, TextField } from '@material-ui/core';
import './JoinComponent.css';
import {observable, action, computed} from "mobx";
import { observer } from 'mobx-react';
import { makeStyles } from '@material-ui/core/styles';

@observer
export class JoinComponent extends React.Component {
  @observable private textInput: string = "";

  render() {
    return (
      <div style={{ alignContent: 'center', display: 'flex', height: "60%" }}>
        <div style={{ flex: '1' }} />
        <div className='join-component-button-area'>
          <div className='join-component-button-area-row'>
            <div className='join-component-button-area-button' />
            <div className='join-component-button-area-button'>
              <Button color='primary' href='/create'>
                New Game!
              </Button>
            </div>
          </div>
          <div className='join-component-button-area-row'>
            <div className='join-component-button-area-button'>
              <form
                className='join-component-form'
                noValidate
                autoComplete='off'>
                <TextField
                  id='game-uuid'
                  label='Spiel-Code'
                  variant='outlined'
                  defaultValue="test"
                  onChange={this.handleInputChange}
                />
              </form>
            </div>
            <div className='join-component-button-area-button'>
              <Button color='primary'>Beitreten</Button>
            </div>
          </div>
        </div>
        <div style={{ flex: '1' }} />
      </div>
    );
  }

  @action.bound
  private handleInputChange(e: any): void{
    this.textInput = e.target.value;
  }



}
