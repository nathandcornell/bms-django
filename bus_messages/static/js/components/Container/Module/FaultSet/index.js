import React from 'react'
import ReactDOM from 'react-dom'

import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import Typography from '@material-ui/core/Typography'

export default class FaultSet extends React.Component {
  render () {
    const { classes, data } = this.props
    const faults = {
      "communication_fault": data.communication_fault,
      "charge_low_warning": data.charge_low_warning,
      "high_voltage_fault": data.high_voltage_fault,
      "high_voltage_warning": data.high_voltage_warning,
      "high_current_fault": data.high_current_fault,
      "high_current_warning": data.high_current_warning,
      "temperature_fault": data.temperature_fault,
      "low_voltage_non_recoverable_fault": data.low_voltage_non_recoverable_fault,
      "low_voltage_warning": data.low_voltage_warning,
      "low_voltage_fault": data.low_voltage_fault,
      "communication_error": data.communication_error,
      "temperature_warning": data.temperature_warning,
    }

    return (
      <Paper className={classes.moduleSection}>
        <Grid container item xs={10} spacing={16}>
          <Grid item xs={4}>
            <Typography component="h6" variant="h6">Faults / Warnings</Typography>
          </Grid>
          <Grid item xs={8}>
            {Object.entries(faults).map(fault => (
              <span key={fault}>
                {(fault[1]) ? fault[0] + ", " : ""}
              </span>
            ))}
          </Grid>
        </Grid>
      </Paper>
    )
  }
}
