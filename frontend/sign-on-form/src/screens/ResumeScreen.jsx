import React from 'react';

export default function ResumeScreen() {
  return (
    <main style={styles.main}>
      <h1>Resume Screen</h1>
      <p>Welcome! This page is currently under construction.</p>
    </main>
  );
}

const styles = {
  main: {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
    textAlign: 'center',
    backgroundColor: '#f0f0f0',
    color: '#333',
    fontFamily: 'Arial, sans-serif',
  },
};
