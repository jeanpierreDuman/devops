<?php

use PHPUnit\Framework\TestCase;

class BasicTest extends TestCase {
    public function testAssert() {
        $this->assertSame(3, 3);
    }
}