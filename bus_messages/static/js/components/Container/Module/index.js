import React from 'react'
import ReactDOM from 'react-dom'

import moment from 'moment'
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import Typography from '@material-ui/core/Typography'

import GaugeSet from './GaugeSet'
import BalancingSet from './BalancingSet'
import FaultSet from './FaultSet'


export default class Module extends React.Component {
  constructor() {
    super()
    this.module_states = {
      'S': 'sleeping',
      'I': 'Initializing',
      'O': 'Off',
      'R': 'Ready',
      'D': 'Discharging',
      'C': 'Charging',
      'F': 'Fault'
    }
  }
  render () {
    const { classes, data } = this.props

    return (
      <Grid item>
        <Paper className={classes.module}>
          <Grid container item xs={12} spacing={16}>
            <Grid item xs={4}>
              <Typography component="h4" variant="h4" gutterBottom>
                {data.serial_no.substr(data.serial_no.length - 5)}
              </Typography>
            </Grid>
            <Grid item xs={4}>
              <Typography component="h6" variant="h6" gutterBottom>
                State: {this.module_states[data.state]}
              </Typography>
            </Grid>
            <Grid item xs={4}>
              <Typography component="h6" variant="h6" gutterBottom>
                {moment(data.created_at).format("lll z")}
              </Typography>
            </Grid>
          </Grid>
          <GaugeSet classes={classes} data={data} />
          <BalancingSet classes={classes} data={data} />
          <FaultSet classes={classes} data={data} />
        </Paper>
      </Grid>
    )
  }
}
