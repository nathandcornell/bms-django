import React from 'react'
import ReactDOM from 'react-dom'

import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import Typography from '@material-ui/core/Typography'

import GaugeSet from './GaugeSet'
import BalancingSet from './BalancingSet'
import FaultSet from './FaultSet'

export default class Module extends React.Component {
  render () {
    const { classes, data } = this.props

    return (
      <Grid item>
        <Paper className={classes.module}>
          <Typography component="h4" variant="h4" gutterBottom>
            {data.serial_no.substr(data.serial_no.length - 5)}
          </Typography>
          <GaugeSet classes={classes} data={data} />
          <BalancingSet classes={classes} data={data} />
          <FaultSet classes={classes} data={data} />
        </Paper>
      </Grid>
    )
  }
}
