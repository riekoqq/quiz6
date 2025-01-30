import Header from './components/Header'
import Footer from './components/Footer';
import { Container } from 'react-bootstrap';
import Homescreen from './screens/HomeScreen';

import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import DrugScreen from './screens/DrugScreen';

function App() {
  return (
    <Router>
        <Header />
          <main className='py-3'>
            <Container>
              <Routes>
                <Route path='/' element={<Homescreen />} exact />
                <Route path='/drug/:id' element={<DrugScreen />} />
              </Routes>
            </Container>
          </main>
        <Footer />
    </Router>
  );
}

export default App;
