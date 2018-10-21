import React from 'react'
import ReactDOM from 'react-dom'

import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import Typography from '@material-ui/core/Typography'
import ReactSpeedometer from "react-d3-speedometer"

export default class Module extends React.Component {
  render () {
    const { classes, data } = this.props

    return (
      <Grid item>
        <Paper className={classes.module}>
          <Typography component="h4" variant="h4" gutterBottom>
            {data.serial_no.substr(data.serial_no.length - 5)}
          </Typography>
          <Paper className={classes.moduleSection}>
            <Grid container item xs={12} spacing={16}>
              <Grid item xs={4}>
                <ReactSpeedometer
                  width={120}
                  height={90}
                  ringWidth={20}
                  minValue={0}
                  maxValue={50}
                  startColor="blue"
                  endColor="purple"
                  value={data.avg_cell_temperature}
                  currentValueText="Temp: ${value}º C"
                />
              </Grid>
              <Grid item xs={4}>
                <ReactSpeedometer
                  width={120}
                  height={90}
                  ringWidth={20}
                  minValue={1.8}
                  maxValue={6.0}
                  value={data.avg_cell_voltage / 1000}
                  currentValueText="Voltage: ${value} V"
                />
              </Grid>
              <Grid item xs={4}>
                <ReactSpeedometer
                  width={120}
                  height={90}
                  ringWidth={20}
                  maxValue={10.0}
                  value={data.amperes}
                  currentValueText="Amperes: ${value}"
                />
              </Grid>
            </Grid>
          </Paper>
        </Paper>
      </Grid>
    )
  }
}
